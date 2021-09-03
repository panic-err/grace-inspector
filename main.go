package main

import (

    "time"
    "fmt"
    "log"
    "os"
    "context"
    "strings"
    "github.com/streadway/amqp"
    "database/sql"
    _ "github.com/go-sql-driver/mysql"
    twilio "github.com/twilio/twilio-go"
    openapi "github.com/twilio/twilio-go/rest/api/v2010"


)


func sendSMS() {
        client := twilio.NewRestClient()
        paramsAPI := openapi.CreateMessageParams{}
        paramsAPI.SetTo(os.Getenv("TO_PHONE_NUMBER"))
        paramsAPI.SetFrom(os.Getenv("TWILIO_PHONE_NUMBER"))
        paramsAPI.SetBody("Hello from gomess!")

        _, err := client.ApiV2010.CreateMessage(&paramsAPI)
        if err != nil {
                panic(err)
        }else {
                fmt.Println("SMS sent!")
        }
}

func failOnError(err error, msg string) {
        if err != nil {
                log.Fatalf("%s: %s", msg, err)
        }
}

func recv() {
        conn, err := amqp.Dial("amqp://"+os.Getenv("CREDS")+"@biggest.dumpster.world:5672/")
        failOnError(err, "Failed to connect to rabbitmq")
        defer conn.Close()

        ch, err := conn.Channel()
        failOnError(err, "Failed to open a channel")
        defer ch.Close()

        err = ch.ExchangeDeclare(
            "logs_topic", //name
            "topic", //type
            true, //durable
            false, //auto-deleted
            false, //internal
            false, //no-wait
            nil, //arguments
        )
        failOnError(err, "Failed to declare an exchange")

        q, err := ch.QueueDeclare(
            "", //name
            false, //durable
            false, //delete when unused
            true, //exclusive
            false, //nowait
            nil, //arguments
        )

        failOnError(err, "Failed to declare a queue")

        if len(os.Args) < 2  {
                log.Printf("Usage: %s [binding_key]..", os.Args[0])
                os.Exit(0)

        }
                s := os.Args[1]
                log.Printf("Binding queue %s to exchange %s with routing key %s", q.Name, "logs_topic", s)

                err = ch.QueueBind(
                    q.Name, //queue name
                    s, //routing key
                    "logs_topic", //exchange
                    false,
                    nil)
                failOnError(err, "Failed to bind a queue")

        msgs, err := ch.Consume(
            q.Name, //queue
            "", //consumer
            true, //auto ack
            false, //exclusive
            false, //nolocal
            false, //no wait
            nil, //args
        )
        failOnError(err, "Failed to register a consumer")

        forever := make(chan bool)

            go func() {
                for d := range msgs {
                    log.Printf(" [x] %s", d.Body)
                    //If the message comes from rabbitmq-proper
                    //The seperator has to be different for messages
                    //Let's use slash
                    if strings.Contains(string(d.Body), "/") {


                    }

                    //If the message is coming from a text message
                    if strings.Contains(string(d.Body), ":") {
                            splitString := strings.Split(string(d.Body), ":")
                            fmt.Println(splitString)
                            db, err := sql.Open("mysql", os.Getenv("WEASELCONN"))
                            if err != nil {
                                os.Exit(0)
                            }
                            defer db.Close()

                            ctx, cancelfunc := context.WithTimeout(context.Background(), 5*time.Second)
                            defer cancelfunc()
                            res, err := db.ExecContext(ctx, "INSERT INTO baaz VALUES('"+splitString[0]+"', "+splitString[1]+", '"+splitString[2]+"', '"+splitString[3]+"');")
                            if err != nil {
                                log.Printf("Error %s when creating DB\n", err)

                            }
                            no, err := res.RowsAffected()
                            if err != nil {
                                log.Printf("Error %s when fetching rows", err)

                            }
                            log.Printf("rows affected %d\n", no)

                            //add SQL for inserting a new entry
                    }
                    if string(d.Body) == "Exit" {
                     log.Printf("Exiting")
                        os.Exit(0)
                    }
                }
            }()
            log.Printf(" [*] Waiting for logs. To exit press Ctrl-C")
            <-forever
}

func generateExit() {
        conn, err := amqp.Dial("amqp://"+os.Getenv("CREDS")+"@biggest.dumpster.world:5672/")
        failOnError(err, "Failed to connect to RabbitMQ")
        defer conn.Close()

        ch, err := conn.Channel()
        failOnError(err, "Failed to open a channel")
        defer ch.Close()

        err = ch.ExchangeDeclare(
                "logs_topic", // name
                "topic",      // type
                true,         // durable
                false,        // auto-deleted
                false,        // internal
                false,        // no-wait
                nil,          // arguments
        )
        failOnError(err, "Failed to declare an exchange")

        body := "Exit"
        err = ch.Publish(
                "logs_topic",          // exchange
                os.Args[1], // routing key
                false, // mandatory
                false, // immediate
                amqp.Publishing{
                        ContentType: "text/plain",
                        Body:        []byte(body),
                })
        failOnError(err, "Failed to publish a message")

        log.Printf(" [x] Sent %s", body)
}

func generate(mess string) {
        conn, err := amqp.Dial("amqp://"+os.Getenv("CREDS")+"@biggest.dumpster.world:5672/")
        failOnError(err, "Failed to connect to RabbitMQ")
        defer conn.Close()

        ch, err := conn.Channel()
        failOnError(err, "Failed to open a channel")
        defer ch.Close()

        err = ch.ExchangeDeclare(
                "logs_topic", // name
                "topic",      // type
                true,         // durable
                false,        // auto-deleted
                false,        // internal
                false,        // no-wait
                nil,          // arguments
        )
        failOnError(err, "Failed to declare an exchange")

        body := mess
        err = ch.Publish(
                "logs_topic",          // exchange
                os.Args[1], // routing key
                false, // mandatory
                false, // immediate
                amqp.Publishing{
                        ContentType: "text/plain",
                        Body:        []byte(body),
                })
        failOnError(err, "Failed to publish a message")

        log.Printf(" [x] Sent %s", body)
}

func bodyFrom(args []string) string {
        var s string
        if (len(args) < 3) || os.Args[2] == "" {
                s = "hello"
        } else {
                s = strings.Join(args[2:], " ")
        }
        return s
}

func severityFrom(args []string) string {
        var s string
        if (len(args) < 2) || os.Args[1] == "" {
                s = "anonymous.info"
        } else {
                s = os.Args[1]
        }
        return s
}



func main() {
    //prepare for qt!
    //recv()

}

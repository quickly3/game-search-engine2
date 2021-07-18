const { Kafka } = require("kafkajs");

const kafka = new Kafka({
    clientId: "my-app",
    brokers: ["localhost:9092"],
});

const producer = kafka.producer();

const run = async () => {
    // Producing

    let messages = [];

    for (let i = 1; i <= 9000; i++) {
        messages.push({
            value: `Hello KafkaJS user! ${i}`,
        });
    }

    await producer.connect();
    await producer
        .send({
            topic: "test-topic",
            messages: messages
        })
        .then(console.log);

    await producer.disconnect();
};

run().catch(console.error);

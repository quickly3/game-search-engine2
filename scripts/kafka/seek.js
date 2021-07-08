const { Kafka } = require("kafkajs");

const kafka = new Kafka({
    clientId: "my-app",
    brokers: ["localhost:9092"],
});

const consumer = kafka.consumer({
    groupId: "test-group",
    maxBytes:100
});

let counter = 0;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

const run = async () => {
    // Consuming
    await consumer.connect();
    let topic = "test-topic"
    await consumer.subscribe({ topic, fromBeginning: true });

    let comsumer_cnt = 0;
    let paused = false;

    consumer.run({ eachMessage: async ({ topic, message }) => true })
    consumer.seek({ topic, offset: 12384 })

};

run().catch(console.error);

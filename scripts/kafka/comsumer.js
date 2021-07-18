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

    const check = ()=>{
        setTimeout(() => {
            comsumer_cnt = 0;
            check();
        }, 1000);
    }
    check();
    // consumer.run({ eachMessage: async ({ topic, message }) => {
    //     console.log({
    //         offset: message.offset,
    //         value: message.value.toString(),
    //     });
    // } })
    // consumer.seek({ topic, partition: 0, offset: 25935 })

    await consumer.run({
        autoCommit: false,
        eachMessage: async ({ topic, partition, message }) => {
            console.log({
                offset: message.offset,
                value: message.value.toString(),
            });
            console.log(message)
            // await sleep(1000)
            next = (parseInt(message.offset)+1)+''
            console.log('next', next)
            consumer.commitOffsets([
                { topic, partition, offset: next }
            ])
            comsumer_cnt++

            console.log(comsumer_cnt)
            if(comsumer_cnt == 10){
                // await sleep(1000)
            }
        },
    });
};

run().catch(console.error);

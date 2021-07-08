const { Kafka } = require('kafkajs')
const kafka = new Kafka({
  clientId: 'my-app',
  brokers: async () => {
    // Example getting brokers from Confluent REST Proxy
    const clusterResponse = await fetch('https://kafka-rest:8082/v3/clusters', {
      headers: 'application/vnd.api+json',
    }).then(response => response.json())
    const clusterUrl = clusterResponse.data[0].links.self

    const brokersResponse = await fetch(`${clusterUrl}/brokers`, {
      headers: 'application/vnd.api+json',
    }).then(response => response.json())

    const brokers = brokersResponse.data.map(broker => {
      const { host, port } = broker.attributes
      return `${host}:${port}`
    })
    console.log(brokers)
    return brokers
  }
})

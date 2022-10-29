const express = require('express')
const app = express()
const port = Number.parseInt(process.env.PORT) || 3333

const config = require('./config')

let preferredDC = config.preferredDC
let workCommand = config.workCommand
const workResults = []

app.use(express.json())

app.get('/api/v1/preferred_datacenter', (req, res) => {
  res.json({
    preferred_datacenter: preferredDC,
  })
})

app.post('/api/v1/preferred_datacenter', (req, res) => {
  newDC = req.body.preferred_datacenter 
  preferredDC = newDC ? newDC.toString() : preferredDC
  res.json({
    preferred_datacenter: preferredDC,
  })
})

app.post('/api/v1/request_work', (req, res) => {
  console.log(req.body)
  res.json({
    ...req.body,
    shell_command: req.body.datacenter_id === preferredDC ? workCommand : ''
  })
})

app.post('/api/v1/work_command', (req, res) => {
  if (req.body.authKey === config.authKey) {
    const newCommand = req.body.workCommand
    workCommand = newCommand ? newCommand : workCommand
    res.json({
      workCommand,
    })
  }
  else {
    res.status(403)
    res.json({
      error: 'Wrong authKey'
    })
  }
})

app.get('/api/v1/results', (req, res) => {
  res.json(workResults)
})

app.post('/api/v1/post_work_results', (req, res) => {
  console.log(`${req.body.datacenter_id} finished a work.`)
  console.log('STDOUT of the work:')
  console.log(req.body.stdout)
  workResults.unshift({
    time: (new Date).toString(),
    stdout: req.body.stdout,
    exitCode: req.body.exit_status,
    datacenter: req.body.datacenter_id,
  })
  res.json({})
})

app.listen(port, () => {
  console.log(`Orchestrator listening on port ${port}`)
})

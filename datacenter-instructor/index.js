const express = require('express')
const app = express()
const port = Number.parseInt(process.env.PORT) || 3333

let preferredDC = 'FR'

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
    shell_command: req.body.datacenter_id === preferredDC ? 'python3 -c "print(22**52)" && sleep 1 && false' : ''
  })
})

app.post('/api/v1/post_work_results', (req, res) => {
  console.log(`${req.body.datacenter_id} finished a work.`)
  console.log('STDOUT of the work:')
  console.log(req.body.stdout)
  res.json({})
})

app.listen(port, () => {
  console.log(`Orchestrator listening on port ${port}`)
})

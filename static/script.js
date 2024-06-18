const startButton = document.getElementById('startButton')
const stopButton = document.getElementById('stopButton')
let pid = 0
startButton.onclick = async () => {
  console.log("hi")
  const response = await fetch('/start_recording')
  const resObject = await response.json()
  console.log('response object', resObject)
  pid = resObject.pid
  console.log('pid: ', pid)
}

stopButton.onclick = () => {
  console.log('stop: ', pid)
  if (pid == 0) {
    return
  }
  fetch('/stop_recording?pid=' + pid.toString())
}
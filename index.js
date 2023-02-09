const app = require('express')();
const PORT = 8086;

app.listen(
    PORT,
    () => console.log(`here http://localhost:${PORT}`)
)
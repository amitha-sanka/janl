const app = require('express')();
const PORT = 8086;

app.get('/activity', (req, res) => {
    res.status(200).send({
        activity: 'SeaWorld',
        hobby: 'amusement park'
    })
});

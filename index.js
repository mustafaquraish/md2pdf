const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const bodyParser = require('body-parser')


const markdownpdf = require('markdown-pdf');
const fs = require('fs');

require('dotenv').config();

const app = express();

app.use(helmet());
app.use(cors());
app.use(express.json());
app.use(express.static('.'))

async function md2pdf(text, res) {
    markdownpdf()
    .from.string(text)
    .to.buffer({}, (err, buf) => {
        if (err) {
            return res.status(500).send(error)
        }
        res.set({
            'Content-Disposition': `inline; filename=output.pdf`,
            'Content-Type': 'application/pdf'
        })
        res.send(buf)
    })
}

app.get('/url/:from.pdf', async (req, res) => {
    text = req.params.from;
    await md2pdf(text, res);
})

app.get('/url/:from', async (req, res) => {
    text = req.params.from;
    await md2pdf(text, res);
})

app.get('/body', async (req, res) => {
    text = req.body;
    if (text !== {}) {
        text = "";
    }
    md2pdf(text,res);
})

app.get('/*', async (req, res) => {
    res.redirect("/")
})


const port = process.env.PORT || 8000;
app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`);
});
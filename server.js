import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import Groq from "groq-sdk";

dotenv.config();

const app = express();

app.use(cors());
app.use(express.json());

const groq = new Groq({
    apiKey: process.env.GROQ_API_KEY,
});

app.post("/generate-caption", async (req, res) => {
    try {
        const { prompt } = req.body;

        const response = await groq.chat.completions.create({
            model: "llama-3.3-70b-versatile",
            messages: [
                {
                    role: "user",
                    content: `Write an engaging Instagram caption for: ${prompt}`,
                },
            ],
        });

        res.json({
            caption: response.choices[0].message.content,
        });
    } catch (err) {
        console.error(err);
        res.status(500).json({
            error: "Failed to generate caption",
        });
    }
});

app.listen(5000, () => {
    console.log("✅ Server running at http://localhost:5000");
});
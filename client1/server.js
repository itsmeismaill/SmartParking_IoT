const express = require('express');
const nodemailer = require('nodemailer');
const cors = require('cors');

const app = express();

app.use(cors());
app.use(express.json());

app.post('/send-email', async (req, res) => {
  try {
    const { to, subject, body, pdfAttachment } = req.body;

    const transporter = nodemailer.createTransport({
      service: 'gmail',
      auth: {
        user: '', // Remplacez par votre adresse e-mail Gmail
        pass: '', // Remplacez par votre mot de passe Gmail
      },
    });

    const mailOptions = {
      from: '', // Remplacez par votre adresse e-mail Gmail
      to,
      subject,
      html: body, // Utilisez l'attribut 'html' pour inclure le contenu HTML
      attachments: [
        {
          filename: 'parking_details.pdf',
          content: pdfAttachment.split(';base64,').pop(),
          encoding: 'base64',
        },
      ],
    };

    await transporter.sendMail(mailOptions);

    res.status(200).json({ message: 'E-mail sent successfully!' });
  } catch (error) {
    console.error('Error sending e-mail:', error);
    res.status(500).json({ error: 'An error occurred while sending the e-mail.' });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

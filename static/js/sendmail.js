function sendMail(contactForm) {
    emailjs.send("gmail", "kipemails", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "contact_message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        });
        return false;
}
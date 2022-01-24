import React, { Component, useState, useEffect } from 'react';
import axios from 'axios';
import '../assets/css/components/Content.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Form, Button } from 'react-bootstrap';
const fs = require('fs');

function Content() {
    const [file, setFile] = useState({
        fileUrl: '',
        file: ''
    });

    useEffect(() => {
        console.log(file);
      });

 
    const onSuubmit = () => {
        
        axios.post("/members",file)
        .then(response => {
            console.log(response)
        })
        .catch(error => {
            console.log(error)
        })
    }

    const onSubmit = () => {
        console.log(file.fileUrl[0])
       
        let reader =  new FileReader();
        reader.readAsDataURL(file.fileUrl[0]);
        reader.onload=(e)=>{
            const answer_array = e.target.result.split(',');
            console.log(e.target.result)
            setFile({
                ...file,
            file: answer_array[1]})
        }
        

        

    };

    const handleChange = (event) => {
        console.log(event.target.files)
        setFile({
            ...file,
            [event.target.name]: event.target.files
        })
        
        
    };

  

    return (
        
        <Container>

            <div >
                <Form.Group controlId="formFile" className="mb-3" method="post" action="/members">
                    <Form.Label>Seleccione el archivo Mp3 a trancribir</Form.Label>
                    <Form.Control type="file" onChange={handleChange} name="fileUrl"/>
                    <Button variant="primary" type="submit" onClick={onSubmit}>submit</Button>
                    <Button variant="primary" type="submit" onClick={onSuubmit}>submit</Button>
                </Form.Group>


            </div>
        </Container>
    )
}
export default Content;
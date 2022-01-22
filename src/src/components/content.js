import React, { Component, useState } from 'react'
import axios from 'axios';
import '../assets/css/components/Content.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Container, Form, Button } from 'react-bootstrap'


function Content() {
    const [file, setFile] = useState({
        fileUrl: '',
        file: ''
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
        console.log(file)
        let reader =  new FileReader();
        reader.readAsDataURL(file.fileUrl[0]);
        reader.onload=(e)=>{
            console.log(e.target.result)
            setFile({
                ...file,
            file: e.target.result})
        }
       

        

    };

    const handleChange = (event) => {
        console.log(event.target.files)
        setFile({
            ...file,
            [event.target.name]: event.target.files
        })
        console.log(file)
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
import React, {useState, useEffect } from 'react';
import axios from 'axios';
import '../assets/css/components/Content.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Form, Button } from 'react-bootstrap';
import Modal from './modal'

function Content() {
    //const [condAlert, setCondAlert] = useState(false)
    const [file, setFile] = useState({
        name: '',
        extension: '',
        fileBase64: ''
    });

    const [openModal,setOpenModal] =useState(false)

    useEffect(() => {
        console.log(file);
        
        
        
      });

 
    

    const onSubmit = () => {
        setOpenModal(true)
      /*
        axios.post("/members",file)
        .then(response => {
            console.log(response.data)
        })
        .catch(error => {
            console.log(error)
        })*/
    };


    const handleChange = (event) => {
        console.log(event.target.files[0].name)
        const name = event.target.files[0].name
        const ext = event.target.files[0].name.split('.')
        const file = event.target.files
        let reader = new FileReader();
        console.log(ext[1])

        if ((ext[1] !== 'mp3') && (ext[1] !=='m4a')){
            alert('no extension')
        }

        reader.readAsDataURL(file[0]);
        reader.onload=(e)=>{
            const filebase64 = e.target.result.split(',');
            setFile({
                ...file,
                name: name,
                extension: ext[1],
                fileBase64: filebase64[1]})
        }
        
        
    };

  

    return (
        
        <Container>

            <div >
                <Form.Group controlId="formFile" className="mb-3" method="post" action="/members">
                    <Form.Label>Seleccione el archivo Mp3 a trancribir</Form.Label>
                    <Form.Control type="file" onChange={handleChange} name="fileUrl"/>
                    <Button variant="primary" type="submit" onClick={onSubmit} >submit</Button>
                </Form.Group>


            </div>
            {openModal && <Modal closeModal={setOpenModal}/>}

        </Container>
    )
}
export default Content;
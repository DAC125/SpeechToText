import React, { useState } from 'react';
import axios from 'axios';
import fileDownload from 'js-file-download';
import '../assets/css/components/Content.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, Form, Button } from 'react-bootstrap';
import Modal from './modal';
import Loading from './loading';

function Content() {

    const [file, setFile] = useState({
        name: '',
        extension: '',
        fileBase64: ''
    });

    const [openModalFormat, setOpenModalFormat] = useState(false)
    const [enableButtonSummit, setEnableButtonSummit] = useState(false)
    const [openLoading, setOpenLoading] = useState(false)
    const [download, setDownload] = useState(false)
    const [txtFile, setTxtFile] = useState()

    const onSubmit = () => {

        setOpenLoading(true)
        axios.post("/transcriptFile", file)
            .then(response => {
                setOpenLoading(false)
                setTxtFile(atob(response.data.file))
                setDownload(true)

            })
            .catch(error => {
                console.log(error)
            })
    };

    const onDownload = () => {
        fileDownload(txtFile, "test.txt")
    }


    const handleChange = (event) => {

        console.log(event.target.files[0].name)
        const name = event.target.files[0].name
        const ext = event.target.files[0].name.split('.')
        const file = event.target.files
        let reader = new FileReader();
        console.log(ext[1])

        if ((ext[1] !== 'mp3') && (ext[1] !== 'm4a')) {
            setOpenModalFormat(true)
            setEnableButtonSummit(false)
            event.target.value = null;
        } else {
            setOpenModalFormat(false)
            setEnableButtonSummit(true)
            reader.readAsDataURL(file[0]);
            reader.onload = (e) => {
                const filebase64 = e.target.result.split(',');
                setFile({
                    ...file,
                    name: name,
                    extension: ext[1],
                    fileBase64: filebase64[1]
                })
            }
        }




    };



    return (

        <Container className='content'>

            <div >
                <Form.Group controlId="formFile" className="mb-3" method="post" action="/members">
                    <Form.Label>Seleccione el archivo mp3 o m4a para trancribir</Form.Label>
                    <Form.Control type="file" onChange={handleChange} name="fileUrl" />

                </Form.Group>
            </div>
            <div className='footer'>
                <Button variant="primary" type="submit" onClick={onSubmit} disabled={!enableButtonSummit} id='submitBtn'> Transcribir Audio</Button>
                {download && <Button variant="primary" type="submit" onClick={onDownload} id='donwloadBtn'> Descargar Archivo</Button>}

            </div>
            <div>
                {openModalFormat && <Modal closeModal={setOpenModalFormat} />}
            </div>
            <div>
                {openLoading && <Loading />}
            </div>
            <div>

            </div>

        </Container>
    )
}
export default Content;
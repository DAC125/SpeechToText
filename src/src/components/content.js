import React from 'react'
import '../assets/css/components/Content.css'
import {Form} from 'react-bootstrap'

function Content(){
    return(
        <div >
            <div>
                <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>Seleccione el archivo Mp3 a trancribir</Form.Label>
                    <Form.Control type="file" />
                </Form.Group>
            </div>
            <div>
                <Form.Group controlId="formFile" className="mb-3">
                    <Form.Label>seleccione el directorio de transcripciones</Form.Label>
                    <Form.Control type="dir" />
                </Form.Group>
            </div>
        
        
        
        
        </div>
    )
}
export default Content;
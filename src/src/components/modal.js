/*import React from 'react'
import '../assets/css/components/Modal.css';

function Modal({ closeModal }) {
    return (
        <div className='modalBackground'>
            <div className='modalContainer'>
                <div className='titleCloseBtn'>
                    <button onClick={() => closeModal(false)}> X </button>
                </div>

                <div className='title'>
                    <h1>Error de formato</h1>
                </div>
                <div className='body'>
                    <p>Archivo seleccionado no compatible. Ingresar archivos en fromato mp3 o m4a</p>
                </div>
                <div className='footer'>
                    <button onClick={() => closeModal(false)}>Aceptar </button>
                </div>
            </div>
        </div>
    );
}

export default Modal*/

import React, {useState, useEffect } from 'react';
import { Button } from 'react-bootstrap';

function Modal({ closeModal }) {
    const [show, setShow] = useState(false);
  
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
  
    return (
      <>
        <Button variant="primary" onClick={handleShow}>
          Launch demo modal
        </Button>
  
        <Modal show={show} onHide={handleClose}>
          <Modal.Header closeButton>
            <Modal.Title>Modal heading</Modal.Title>
          </Modal.Header>
          <Modal.Body>Woohoo, you're reading this text in a modal!</Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={handleClose}>
              Close
            </Button>
            <Button variant="primary" onClick={handleClose}>
              Save Changes
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
  
  export default Modal
import React from 'react'
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
                    <button onClick={() => closeModal(false)} id='errorBtn'>Aceptar </button>
                </div>
            </div>
        </div>
    );
}

export default Modal


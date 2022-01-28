import React from 'react'
import '../assets/css/components/Modal.css';
import RingLoader from 'react-spinners/RingLoader'
function Loading() {
    return (
        <div className='modalBackground'>
            <div className='modalContainer'>
                <div className='title'>
                    <h1>Transcribiendo audio...</h1>
                </div>
                <div className='body'>
                    <p>Por favor espere, su audio esta siendo procesado. Esto puede tomar unos minutos</p>
                </div>
                <div className='footer'>
                    <RingLoader color={'#140e39'} loading={true}  size={60}/>

                </div>

            </div>
        </div>
    );
}

export default Loading
import React from 'react'
import {Toolbar, AppBar} from '@material-ui/core'
import tec_logo from '../assets/img/logo.svg'
import '../assets/css/components/Navbar.css'

function Navbar(){
    return(
        <div>
            <AppBar position="static" className='navbar'> 
                <Toolbar>
                    <div>
                        <img src={tec_logo} alt="" width="100%" height="100%"/>
                    </div>
                </Toolbar>
            </AppBar>
        </div>
    );
}
export default Navbar;
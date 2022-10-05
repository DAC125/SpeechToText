import React from 'react';
import Navbar from './Navbar';
import Content from './content';
//import {div} from '@material-ui/core';


function Container(){
    return(
    <div>
        <div>
            <div >
                <Navbar></Navbar>
            </div>
            <div >
                <div >
                    <Content></Content>
                </div>
            </div>
        </div>
         
    </div>
    );
}
export default Container;
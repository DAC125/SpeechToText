import React from 'react';
import Navbar from './Navbar';
import Content from './content';
import {Grid} from '@material-ui/core';


function Container(){
    return(
    <div>
        <Grid container>
            <Grid xs={12}>
                <Navbar></Navbar>
            </Grid>
            <Grid container>
                <Grid xs={12}>
                    <Content></Content>
                </Grid>
            </Grid>
        </Grid>
         
    </div>
    );
}
export default Container;
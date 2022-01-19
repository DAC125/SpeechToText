import React, { Component, useState } from 'react'
import '../assets/css/components/Content.css'
import 'bootstrap/dist/css/bootstrap.min.css'
import { Container, Form, Button } from 'react-bootstrap'

/*
class Content extends Component{
    constructor(props) {
        super(props);
        this.state = {
            file: ''
        }
    }
    const [file, setFile] = useState();


    onChange(e){
        let files = e.target.files;

        let reader =  new FileReader();
        reader.readAsDataURL(files[0]);
        reader.onload=(e)=>{
            this.setState({[e.target.name]: e.target.result})
            console.warn("file data",e.target.result);
        }
    };

    render(){
        return (
            <Container>

            <div >


                <Form.Group controlId="formFile" className="mb-3" method="post" action="/members">
                    <Form.Label>Seleccione el archivo Mp3 a trancribir</Form.Label>
                    <Form.Control type="file" onChange={(e)=>this.onChange(e)}/>
                </Form.Group>


            </div>
        </Container>
        )
    }
}
export default Content;*/

function Content() {
    const [file, setFile] = useState({
        fileUrl: '',
        file: ''
    });

    const onSubmit = () => {
        console.log(file.fileUrl)
        let reader =  new FileReader();
        reader.readAsDataURL(file.fileUrl[0]);
        reader.onload=(e)=>{
            console.log(e.target.result)
            /*setFile({
                ...file
            [e.target.name]: e.target.result})*/
        }

    };

    const handleChange = (event) => {
        console.log(event.target.files)
        setFile({
            ...file,
            [event.target.name]: event.target.files
        })
    };

    /*const handleChange(event) {
        let fieldName = event.target.name;
        let fleldVal = event.target.value;
        this.setState({form: {...this.state.form, [fieldName]: fleldVal}})
      }*/

    return (
        
        <Container>

            <div >
                <Form.Group controlId="formFile" className="mb-3" method="post" action="/members">
                    <Form.Label>Seleccione el archivo Mp3 a trancribir</Form.Label>
                    <Form.Control type="file" onChange={handleChange} name="fileUrl"/>
                    <Button variant="primary" type="submit" onClick={onSubmit}>submit</Button>
                </Form.Group>


            </div>
        </Container>
    )
}
export default Content;
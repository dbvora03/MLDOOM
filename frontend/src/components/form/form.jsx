import React from 'react';

import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

import './form.css'

const Form = () => {

    return (
        <div className="formClass">
            <Button variant="contained" color="primary" style={{"height":"55px", "width":"100px"}}>Submit</Button>

        </div>
      );
}
 
export default Form
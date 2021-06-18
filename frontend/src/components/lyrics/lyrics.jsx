import React from 'react';

import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';

import './lyrics.css'

const Lyrics = () => {

    return (
        <div className="formClass">
            <h1>Enter word count</h1>
            <div className="float-container">
                <div className="float-child" style={{"float":"left", "width":"200px"}}>
                    <TextField id="outlined-basic" label="Outlined" variant="outlined" />
                </div>
                <div className="float-child" style={{"float":"right"}}>
                <Button variant="contained" color="primary" style={{"height":"55px", "width":"100px"}}>Submit</Button>
                </div>
            </div>

        </div>
      );
}
 
export default Lyrics
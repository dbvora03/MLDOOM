import './App.css';
import Button from '@material-ui/core/Button';
import {useState} from 'react'
import nl2br from 'react-nl2br'


function App() {

  const [lyrics, setLyrics] = useState("")

  const Submit = () => {

    fetch('http://127.0.0.1:5000/getPhrases', {
      method: "GET",
      headers: {
        'Content-Type': 'application/json',
      }
    }).then(res=> res.json()).then((result)=> {
      let results = result.lyrics[0]
      setLyrics(nl2br(results))
    })

  }

  return (
    <div className="App">
      <div>
        <div class="main-text">
          <h1 className="theTitle"> ML DOOM</h1>
          <p className="theDescription"> An AI that generates MF DOOM like bars</p>
          <Button className="child" variant="contained" color="secondary" style={{"height":"55px", "width":"200px"}} onClick={()=>Submit()}>Generate Lyrics</Button>
        </div>
        <p className="the-lyrics"><strong>{lyrics}</strong></p>
      </div>
    </div>
  );
}

export default App;

import { useEffect, useState } from 'react';
var axios = require('axios');
var FormData = require('form-data');
var data = new FormData();

const imageComponent = (image) => {
  return ( 
    <div className="image">
      <img src={URL.createObjectURL(image)} alt="" />
    </div>
   );
}
 


function App() {
  const [image, setImage] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const onFileChange = (event) =>{
    setImage(event.target.files[0]);
  }
  useEffect(() => {
    console.log(image);
  },[image])

  const onFileUpload = ()=>{
    data.append('file', image);
    var config = {
      method: 'post',
      url: 'http://localhost:8000/',
      headers: { 
        'accept': 'application/json', 
        'Content-Type': 'multipart/form-data', 
      },
      data : data
    };
    
    axios(config)
    .then(function (response) {
      console.log(response.data);
      setPrediction(JSON.stringify(response.data));
    })
    .catch(function (error) {
      console.log(error);
    });
  };
  return (
    <div className="App">
      <center>
        {image?<img src={URL.createObjectURL(image)} alt="" />:
        <div className="waiting">
          Waiting for image
        </div>
        }
        
        <form>
          <center>
            <input type="file" name="Upload File" id="file-button" onChange={onFileChange }/>
            <br />
            <input type="button" value="upload" onClick={onFileUpload} />
          </center>
        </form>
        {prediction?
        <div className="result">
          Result: {JSON.parse(prediction).result} <br />
          Model Prediction:  {JSON.parse(prediction).prediction}
        </div>
        :""}
      </center>
      

    </div>
  );
}

export default App;

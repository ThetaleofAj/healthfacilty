import React from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { MDBContainer, MDBRow, MDBCol, MDBBtn } from "mdbreact";

function Login(){
   const [username, setUserName] = useState();
   const [password, setPassword] = useState();
   //const [token,setToken] = useState();
   let navigate = useNavigate();


   const credentials=(credentials)=>{
      fetch('http://127.0.0.1:8000/rest-auth/login/',{
         method: 'POST',
         headers:{
            'Content-Type': 'application/json'
         },
         body: JSON.stringify(credentials)
      })
      .then(data => data.json())
      .then((result)=>{
         console.log(result.key)
         localStorage.setItem('token',result.key)
         localStorage.setItem('name',username)
         if(result.status_code !== 400){
            navigate('/')
         }else{
            window.alert('Login credentials wrong!')
         }
      },(error)=>{
         console.log('error')
      })
   }

   const handleSubmit=e=>{
      e.preventDefault();
      const token = credentials({
         username,
         password
      })
      console.log(token)
   }

   return(
      <div className="thisView">
      <MDBContainer>
      <MDBRow>
        <MDBCol md="6">
          <form>
            <p className="h4 text-center mb-4">Sign in</p>
            <label htmlFor="defaultFormLoginEmailEx" className="grey-text">
              USERNAME
            </label>
            <input
              type="email"
              id="defaultFormLoginEmailEx"
              className="form-control"
              onChange={e => setUserName(e.target.value)}
            />
            <br />
            <label htmlFor="defaultFormLoginPasswordEx" className="grey-text">
              PASSWORD
            </label>
            <input
              type="password"
              id="defaultFormLoginPasswordEx"
              className="form-control"
              onChange={e => setPassword(e.target.value)}
            />
            <div className="text-center mt-4">
              <MDBBtn color="indigo" type="submit" onClick={handleSubmit} >
                Login
              </MDBBtn>
            </div>
          </form>
        </MDBCol>
      </MDBRow>
    </MDBContainer>
      </div>
   )
}
 export default Login;
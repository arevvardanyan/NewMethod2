import React from "react";
import axios from "axios";
import './Dropdown.css'

class Dropdown extends React.Component{
    state = {
        db: [],
    }
    componentDidMount(){
        let data;
        axios.get('http://localhost:8000/category/')
        .then(res=>{
            data = res.data;
            this.setState({
                db:data
            })
        })
        .catch(err=>{})
    }
    renderSwitch = (param) =>{
        switch(param + 1){
            case 1:
                return "primary";
            case 2:
                return  "second";
            case 3:
                return "succes";
            case 4:
                return "danger";
            case 5:
                return  "warning";
            case 6:
                return "info";
            default:
                return "yellow"               
        }
    }

    render(){
    return ( 
        <div className="container-jumbotron " style={{position:"absolute"}}> 
            

            {this.state.db.map((detail, id) => ( 
                <div key={id} className ={'dropdown-' + this.renderSwitch(id % 6)} > 
                
                    <ul className={'dr-li' + this.renderSwitch(id % 6)}>
                        <li>{detail.name}</li>
                    </ul>
                    
                </div> 
            ))} 
        </div> 
    ); 
}
}




export default Dropdown
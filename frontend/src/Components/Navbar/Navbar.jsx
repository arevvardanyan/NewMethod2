import React, { useState } from 'react'
import './Navbar.css'
import cart_icon from '../Assets/cart-icon.png'
import login_icon from '../Assets/person-icon.png'
import threeLine from '../Assets/3line.png'
import robot from '../Assets/robot.png'
import search from '../Assets/search.png'

import { Link } from 'react-router-dom'
import Dropdown from '../DropDown/Dropdown'

const Navbar = () =>{
    const [menu, setMenu] = useState("New In")
    const [openMenu, setOpenMenu] = useState(false)
    return(
        <div className='navbar'>
         <div className='navbar-up'>
              
        <h1><Link style={{textDecoration:'none',color:'white'}} to="/">Sellforia</Link> </h1>

        <ul className='nav-menu'>
            <li onClick={()=>{setMenu("new in")}}><Link style={{textDecoration:'none',color:'white'}} to='/new in'> New In</Link> {menu==="new in"?<hr/>:<></>}</li>
            <li onClick={()=>{setMenu("stores")}}><Link style={{textDecoration:'none',color:'white'}} to='/stores'>Stores</Link>  {menu==="stores"?<hr/>:<></>}</li>
            <li onClick={()=>{setMenu("our mission")}}><Link style={{textDecoration:'none',color:'white'}} to='/our mission'>Our Mission</Link> {menu==="our mission"?<hr/>:<></>}</li>
            <li onClick={()=>{setMenu("settings")}}><Link style={{textDecoration:'none',color:'white'}} to='/settings'>Settings</Link> {menu==="settings"?<hr/>:<></>}</li>
        </ul>

        <div className='nav-login-cart'>
            <button><Link style={{textDecoration:'none',color:'white'}} to='login'>Log In</Link> </button>
            <Link style={{textDecoration:'none'}} to='user'><img className='login-icon' src={login_icon} alt="" /></Link>
            <Link style={{textDecoration:'none'}} to='/cart'><img className='cart-icon' src={cart_icon} alt="" /></Link>
            
            <div className="nav-cart-count">0</div>
        </div>
        </div> 
        <div className="navbar-down">
            <img src={threeLine} alt="" onClick={()=>setOpenMenu((prev)=>!prev)} />
            <div className='search-bar'>
            <img src={robot} alt="" />
            <div className='searchAndIcon'>
            <input type="search" className='search-form' />
            <img src={search} alt="" />
            </div>
            </div>
        </div>
        {
            openMenu && <Dropdown />
        }
        
        </div>
        

        
    )
}

export default Navbar
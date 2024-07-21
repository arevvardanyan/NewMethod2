import './App.css';
import Navbar from './Components/Navbar/Navbar';
import {BrowserRouter,Routes,Route}  from 'react-router-dom'
import ShopCategory from './pages/ShopCategory';
import Cart from './pages/Cart';
import LoginSignUp from './pages/LoginSignUp';
import Shop from './pages/Shop'
import User from './pages/User';
import DataFetchingComponent from './Components/Data/DataFetchingComponent';


function App() {
  return (
    <div >
      <BrowserRouter>

        <Navbar />

        <Routes>
          
          <Route path='/' element={<Shop/>}/>
          <Route path='/new in' element={<ShopCategory category="new in"/>}/>
          <Route path='/stores' element={<ShopCategory category="stores"/>}/>
          <Route path='/our mission' element={<ShopCategory category="our mission"/>}/>
          <Route path='settings' element={<ShopCategory category="settings"/>}/>
          <Route path='/login' element={<LoginSignUp/>}/>
          <Route path='/user' element={<User/>}/>
          <Route path='/cart' element={<Cart/>}/>  
        </Routes>

      </BrowserRouter>
      
    </div>
  );
}

export default App;

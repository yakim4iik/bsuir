import './App.css';
import {BrowserRouter} from 'react-router-dom';
import AppRouter from './components/AppRouter';
import Header from './components/Header';
import 'bootstrap/dist/css/bootstrap.min.css';
import {observer} from "mobx-react-lite";

function App() {


    return (
        <BrowserRouter>
            <Header/>
            <AppRouter/>
            <div style={{height: '20px'}}></div>
        </BrowserRouter>
    );
}

export default observer(App);

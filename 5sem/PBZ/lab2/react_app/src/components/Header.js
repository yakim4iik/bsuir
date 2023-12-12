import {NavLink} from 'react-router-dom';
import {observer} from 'mobx-react-lite';


function Header() {
    return (
        <header>
            <h2 style={{color: 'white', margin: '10px 20px'}}><NavLink className='simple-link hover-disable'
                                                                       to={'/'}>Learning for employees</NavLink></h2>
        </header>
    )
}

export default observer(Header);
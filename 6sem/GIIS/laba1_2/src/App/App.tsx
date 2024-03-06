import { useState } from 'react'

import Lab1 from '../Lab1/Lab1'
import Lab2 from '../Lab2/Lab2'

import './App.css'

function App() {
	const [selectedLab, setSelectedLab] = useState(1)

	const handleLabChange = (labNumber: number) => {
		setSelectedLab(labNumber)
	}

	return (
		<div className='MainWrapper'>
			<div className='Main'>
				<div className='LabSelection'>
					<label>Лабораторная </label>
					<div>
						<button
							className={selectedLab === 1 ? 'selected' : ''}
							onClick={() => handleLabChange(1)}
						>
							1
						</button>
						<button
							className={selectedLab === 2 ? 'selected' : ''}
							onClick={() => handleLabChange(2)}
						>
							2
						</button>
					</div>
				</div>
				{selectedLab === 1 && <Lab1 />}
				{selectedLab === 2 && <Lab2 />}
			</div>
		</div>
	)
}

export default App

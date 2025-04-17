import './App.css'
import Table from './table'
import Timer from './timer'
import Quote from './quote'
import { useState } from 'react'

function App() {

  const [laps, addLaps] = useState([]);
  const [quoteRefreshTrigger, setQuoteRefreshTrigger] = useState(0);
  
  const appendLaps = (lap) => {
    addLaps((prev) => [...prev, lap])
  }
  
  const refreshQuote = () => {
    setQuoteRefreshTrigger(prev => prev + 1);
  }

  return (
    <>
      <Timer appendLaps={appendLaps} refreshQuote={refreshQuote} />
      <Quote refreshTrigger={quoteRefreshTrigger} />
      <Table laps={laps} />
    </>
  )
}

export default App

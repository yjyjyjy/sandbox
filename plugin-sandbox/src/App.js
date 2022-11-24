import { useState } from 'react';
import './App.css';
import NoteTaker from './components/NoteTaker';
import RinaBadge from './components/RinaBadge';

function App() {
  const [noteExpanded, setNoteExpanded] = useState(false)
  return (
    <div className="App">
      {noteExpanded ? <NoteTaker setNoteExpanded={setNoteExpanded} />
        : <RinaBadge setNoteExpanded={setNoteExpanded} />}
    </div>
  );
}

export default App

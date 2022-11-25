import { createContext, useState } from 'react';
import './App.css';
import NoteTaker from './components/NoteTaker';
import RinaBadge from './components/RinaBadge';

export const RinaNoteContxt = createContext(null)

function App() {
  const [template, setTemplate] = useState(null)
  const [templateOptions, setTemplateOptions] = useState([
    "Backend Eng",
    "Frontend Eng",
    "Data Eng"
  ])
  const [note, setNote] = useState('')

  const [noteExpanded, setNoteExpanded] = useState(false)
  return (
    <RinaNoteContxt.Provider
      value={{
        template, setTemplate,
        templateOptions, setTemplateOptions,
        note, setNote
      }}
    >
      <div className="App">
        {noteExpanded ? <NoteTaker setNoteExpanded={setNoteExpanded} />
          : <RinaBadge setNoteExpanded={setNoteExpanded} />}
      </div>
    </RinaNoteContxt.Provider>
  );
}

export default App

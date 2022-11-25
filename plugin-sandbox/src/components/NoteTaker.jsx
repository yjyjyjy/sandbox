import { CgCloseR } from "react-icons/cg";
import { GiPlainCircle } from "react-icons/gi";
import { GiPauseButton } from "react-icons/gi";
import { useContext } from "react";
import DropDownMenu from "./DropDownMenu";
import { RinaNoteContxt } from "../App";

const NoteTaker = ({ setNoteExpanded }) => {
    const { note, setNote, isRecording, setIsRecording } = useContext(RinaNoteContxt)

    return (
        <div
            className='absolute h-[500px] w-[400px] min-h-[300px] min-w-[300px] flex flex-col overflow-hidden resize left-10 top-10 shadow-lg rounded-md bg-white border'
            style={{ zIndex: 1000 }}
        >
            {/* header */}
            <div className="h-8 w-full rounded-t-md bg-indigo-500 flex items-center justify-between px-4">
                <div className="text-white">
                    <span>Rina</span>
                    {isRecording && <span className="ml-4 text-xs">recording...</span>}
                </div>
                <CgCloseR
                    className="text-white hover:text-gray-200 cursor-pointer"
                    onClick={() => setNoteExpanded(false)}
                />
            </div>

            <div className="w-full h-full flex flex-col overflow-hidden">
                {/* Control Panel */}
                <div className="flex justify-between px-4 py-1 text-slate-700">
                    <div className="flex justify-start items-center space-x-2 pl-2">
                        <GiPlainCircle
                            className={"text-red-500 cursor-pointer" + (isRecording ? ' Recording-blinking' : '')}
                            onClick={() => { setIsRecording(!isRecording) }}
                        />
                        <GiPauseButton
                            className="cursor-pointer"
                            onClick={() => setIsRecording(false)}
                        />
                    </div>
                    <div>
                        <DropDownMenu />
                    </div>
                </div>

                {/* Note taking */}
                <div className="py-2 px-4 flex flex-col h-full">
                    {/* TODO: Name, Role, Round, Interviewer */}
                    <label htmlFor="comment" className="block text-sm font-medium text-gray-700">
                        Interview Note
                    </label>
                    <textarea
                        name="note"
                        id="rina-note-textarea"
                        className="w-full h-full grow rounded-md border border-gray-200 focus:border-indigo-500 shadow-sm my-2 sm:text-sm p-2"
                        defaultValue={''}
                        value={note}
                        onChange={e => setNote(e.target.value)}
                    />
                </div>
            </div>
        </div>
    );
};

export default NoteTaker;
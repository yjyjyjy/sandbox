import { CgCloseR } from "react-icons/cg";
import { GiPlainCircle } from "react-icons/gi";
import { FaStop } from "react-icons/fa";
import { useState } from "react";
import DropDownMenu from "./DropDownMenu";


const NoteTaker = ({ setNoteExpanded }) => {

    const [isRecording, setIsRecording] = useState(false)
    return (
        <div
            className='absolute h-[500px] w-[400px] left-10 top-10 shadow-lg rounded-md flex-col justify-center items-center bg-white border'
            style={{ zIndex: 1000 }}
        >
            {/* header */}
            <div className="h-8 w-full rounded-t-md bg-indigo-500 flex items-center justify-between px-4">
                <span className="text-white">Rina</span>
                <CgCloseR
                    className="text-white hover:text-gray-200 cursor-pointer"
                    onClick={() => setNoteExpanded(false)}
                />
            </div>

            {/* Control Panel */}
            <div className="flex justify-between px-4 py-1 text-slate-700">
                <div className="flex justify-start items-center space-x-2 pl-2">
                    <GiPlainCircle className="text-red-500" />
                    <FaStop />
                    {isRecording && <span>recording...</span>}
                </div>
                <div>
                    <DropDownMenu />
                </div>
            </div>

            {/* Note taking */}
            <div className="py-2 px-4">
                <label htmlFor="comment" className="block text-sm font-medium text-gray-700">
                    Add your comment
                </label>
                <div className="mt-1">
                    <textarea
                        rows={10}
                        name="comment"
                        id="comment"
                        className="block w-full rounded-md border border-gray-200 shadow-sm sm:text-sm p-2"
                        defaultValue={''}
                    />
                </div>
            </div>
        </div>
    );
};

export default NoteTaker;
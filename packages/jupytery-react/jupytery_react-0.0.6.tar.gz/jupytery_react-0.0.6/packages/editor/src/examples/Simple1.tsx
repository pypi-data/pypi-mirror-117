import { useState, useMemo } from 'react';
import { createEditor, Descendant } from 'slate';
import { Slate, Editable, withReact } from 'slate-react';

const Simple1 = () => {
  const editor = useMemo(() => withReact(createEditor()), []);
  const [value, setValue] = useState<Descendant[]>([
    {
      type: 'paragraph',
      children: [{ text: 'Simple Editor' }],
    },
  ]);
  return (
    <Slate editor={editor} value={value} onChange={value => setValue(value)}>
      <Editable />
    </Slate>
  );
}

export default Simple1;

from typing import Optional
from pydantic import BaseModel


class ResourceBase(BaseModel):
    title: str = None
    description: str = None
    category: str = None
    format: str = None
    type: str = None
    content: str = None
    keyword: list[str] = None
    difficulty: int = None


class ResourceNoneInteraction(ResourceBase):
    pass


class ResourceInteraction(ResourceBase):
    pass


class ResourceCreate(BaseModel):
    pass


class TestResourceNoneInteraction(ResourceBase):
    title: str = "Python第一个程序"
    description: str = "Python第一个简单程序的代码实现与讲解"
    category: str = "Python Intro"
    format: str = "text"
    type: str = "code"
    content: str = "<code># Script Begins print(\"GeeksQuiz\") # Scripts Ends</code><p>Output:</p><pre>GeeksQuiz</pre> <p><em><strong> 第一行：[</strong></em><strong># Script Begins]</strong>在 Python 中，注释以 # 开头。该语句被解释器忽略并用作我们代码的文档。</p><p><em><strong>第二行： </strong><strong>[</strong><strong>print(&#8220;GeeksQuiz&#8221;)] </strong></em> 为了在控制台上打印一些内容，使用了 print() 函数。此函数还在我们的消息打印后添加一个换行符（与 C 不同）。请注意，在 Python 2 中，“print”不是函数而是关键字，因此可以不带括号使用。但是，在 Python 3 中，它是一个函数，必须用括号调用。</p><p><em><strong>第三行： [</strong></em><strong># Script Ends]</strong>这只是同第 1 行中的另一个注释.</p>"


class TestResourceInteraction(ResourceBase):
    title: str = "test"
    description: str = "test"
    category: str = "test"
    format: str = "test"
    content: dict[str, str] = {
        "question": "What will be the output of the following code : <code>\nprint type(type(int))\n",
        "choices": {1: "type 'int'",
                    2: "type 'type'",
                    3: "Error",
                    4: '0'},
        "a": 2}
    keyword: list[str] = ['function', 'python function']
    difficulty: int = 1

<div class="ql-snow next-bvymu8 e1hv24360">
  <div class="ql-editor">
    <p>
      <strong class="ql-size-huge">Покрокова інструкція виконання фінального проєкту</strong>
    </p>
    <p><br></p>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 1. Структури даних. Сортування. Робота з однозв'язним
        списком</strong>
    </p>
    <p><br></p>
    <p>
      Для реалізації однозв'язного списку (приклад реалізації можна взяти з
      конспекту) необхідно:
    </p>
    <ul>
      <li>
        написати функцію, яка реалізує реверсування однозв'язного списку,
        змінюючи посилання між вузлами;
      </li>
      <li>
        розробити алгоритм сортування для однозв'язного списку, наприклад,
        сортування вставками або злиттям;
      </li>
      <li>
        написати функцію, що об'єднує два відсортовані однозв'язні списки в один
        відсортований список.
      </li>
    </ul>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою
        рекурсії</strong>
    </p>
    <p><br></p>
    <p>
      Необхідно написати програму на Python, яка використовує рекурсію для
      створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал
      “дерево Піфагора”, і користувач повинен мати можливість вказати рівень
      рекурсії.
    </p>
    <div class="ql-custom-image" contenteditable="false" align="center" data-blot-name="custom-image" data-id="gchn7" data-src="https://s3.eu-north-1.amazonaws.com/lms.goit.files/9ed4edf8-bfc6-4e09-bb32-3aeef75b381cUntitled%20%2822%29.png" data-width="300px" data-height="auto">
      <div class="next-1bk4wn6 e11xll1g1">
        <img class="ql-custom-image" id="gchn7" src="https://s3.eu-north-1.amazonaws.com/lms.goit.files/9ed4edf8-bfc6-4e09-bb32-3aeef75b381cUntitled%20%2822%29.png"><button>
          <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#fullscreenExpand_svg__a)" fill="currentcolor">
              <path d="M20 19.063V.938A.939.939 0 0 0 19.062 0H.938A.939.939 0 0 0 0 .938v5.625a.312.312 0 1 0 .625 0V.938A.313.313 0 0 1 .938.625h18.125a.313.313 0 0 1 .312.313v18.125a.313.313 0 0 1-.313.312h-5.625a.313.313 0 1 0 0 .625h5.626c.516 0 .937-.42.937-.938Z"></path>
              <path d="M.938 8.125A.939.939 0 0 0 0 9.063v10c0 .516.42.937.938.937h10c.516 0 .937-.42.937-.938V8.568l4.375-4.375v4.245a.312.312 0 1 0 .625 0v-5a.312.312 0 0 0-.313-.312h-5a.313.313 0 1 0 0 .625h4.245l-4.375 4.375H.938ZM11.25 19.063a.313.313 0 0 1-.313.312h-10a.312.312 0 0 1-.312-.313v-10a.312.312 0 0 1 .313-.312H11.25v10.313Z"></path>
            </g>
            <defs>
              <clipPath id="fullscreenExpand_svg__a">
                <path fill="#fff" d="M0 0h20v20H0z"></path>
              </clipPath>
            </defs>
          </svg>
        </button>
      </div>
    </div>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 3. Дерева, алгоритм Дейкстри</strong>
    </p>
    <p><br></p>
    <p>
      Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому
      графі, використовуючи бінарну купу. Завдання включає створення графа,
      використання піраміди для оптимізації вибору вершин та обчислення
      найкоротших шляхів від початкової вершини до всіх інших.
    </p>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 4. Візуалізація піраміди</strong>
    </p>
    <p><br></p>
    <p>
      Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб
      зрозуміти, як він працює.
    </p>
    <p><br></p>
    <div class="ql-syntax-block">
      <pre class="ql-syntax ql-block-style-code hljs language-routeros" spellcheck="false" data-highlighted="yes">import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
&nbsp;&nbsp;def __init__(self, key, <span class="hljs-attribute">color</span>=<span class="hljs-string">"skyblue"</span>):
&nbsp;&nbsp;&nbsp;&nbsp;self.left = None
&nbsp;&nbsp;&nbsp;&nbsp;self.right = None
&nbsp;&nbsp;&nbsp;&nbsp;self.val = key
&nbsp;&nbsp;&nbsp;&nbsp;self.color = color&nbsp;# Додатковий аргумент для зберігання кольору вузла
&nbsp;&nbsp;&nbsp;&nbsp;self.id = str(uuid.uuid4())&nbsp;# Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, <span class="hljs-attribute">x</span>=0, <span class="hljs-attribute">y</span>=0, <span class="hljs-attribute">layer</span>=1):
&nbsp;&nbsp;<span class="hljs-keyword">if</span> node is <span class="hljs-keyword">not</span> None:
&nbsp;&nbsp;&nbsp;&nbsp;graph.add_node(node.id, <span class="hljs-attribute">color</span>=node.color, <span class="hljs-attribute">label</span>=node.val)&nbsp;# Використання id та збереження значення вузла
&nbsp;&nbsp;&nbsp;&nbsp;<span class="hljs-keyword">if</span> node.left:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graph.add_edge(node.id, node.left.id)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l = x - 1 / 2 ** layer
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pos[node.left.id] = (l, y - 1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;l = add_edges(graph, node.left, pos, <span class="hljs-attribute">x</span>=l, <span class="hljs-attribute">y</span>=y - 1, <span class="hljs-attribute">layer</span>=layer + 1)
&nbsp;&nbsp;&nbsp;&nbsp;<span class="hljs-keyword">if</span> node.right:
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;graph.add_edge(node.id, node.right.id)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r = x + 1 / 2 ** layer
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;pos[node.right.id] = (r, y - 1)
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;r = add_edges(graph, node.right, pos, <span class="hljs-attribute">x</span>=r, <span class="hljs-attribute">y</span>=y - 1, <span class="hljs-attribute">layer</span>=layer + 1)
&nbsp;&nbsp;return graph


def draw_tree(tree_root):
&nbsp;&nbsp;tree = nx.DiGraph()
&nbsp;&nbsp;pos = {tree_root.id: (0, 0)}
&nbsp;&nbsp;tree = add_edges(tree, tree_root, pos)

&nbsp;&nbsp;colors = [node[1][<span class="hljs-string">'color'</span>] <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> tree.nodes(<span class="hljs-attribute">data</span>=<span class="hljs-literal">True</span>)]
&nbsp;&nbsp;labels = {node[0]: node[1][<span class="hljs-string">'label'</span>] <span class="hljs-keyword">for</span> node <span class="hljs-keyword">in</span> tree.nodes(<span class="hljs-attribute">data</span>=<span class="hljs-literal">True</span>)}&nbsp;# Використовуйте значення вузла для міток

&nbsp;&nbsp;plt.figure(figsize=(8, 5))
&nbsp;&nbsp;nx.draw(tree, <span class="hljs-attribute">pos</span>=pos, <span class="hljs-attribute">labels</span>=labels, <span class="hljs-attribute">arrows</span>=<span class="hljs-literal">False</span>, <span class="hljs-attribute">node_size</span>=2500, <span class="hljs-attribute">node_color</span>=colors)
&nbsp;&nbsp;plt.show()


<span class="hljs-comment"># Створення дерева</span>
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

<span class="hljs-comment"># Відображення дерева</span>
draw_tree(root)
</pre>
      <button class="copy"></button>
    </div>
    <p><br></p>
    <div class="ql-custom-image" contenteditable="false" align="center" data-blot-name="custom-image" data-id="9c0c7" data-src="https://s3.eu-north-1.amazonaws.com/lms.goit.files/4dc212c2-e9d6-4f8f-822a-7d268fcc7148Untitled%20%2823%29.png" data-width="300px" data-height="auto">
      <div class="next-1bk4wn6 e11xll1g1">
        <img class="ql-custom-image" id="9c0c7" src="https://s3.eu-north-1.amazonaws.com/lms.goit.files/4dc212c2-e9d6-4f8f-822a-7d268fcc7148Untitled%20%2823%29.png"><button>
          <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#fullscreenExpand_svg__a)" fill="currentcolor">
              <path d="M20 19.063V.938A.939.939 0 0 0 19.062 0H.938A.939.939 0 0 0 0 .938v5.625a.312.312 0 1 0 .625 0V.938A.313.313 0 0 1 .938.625h18.125a.313.313 0 0 1 .312.313v18.125a.313.313 0 0 1-.313.312h-5.625a.313.313 0 1 0 0 .625h5.626c.516 0 .937-.42.937-.938Z"></path>
              <path d="M.938 8.125A.939.939 0 0 0 0 9.063v10c0 .516.42.937.938.937h10c.516 0 .937-.42.937-.938V8.568l4.375-4.375v4.245a.312.312 0 1 0 .625 0v-5a.312.312 0 0 0-.313-.312h-5a.313.313 0 1 0 0 .625h4.245l-4.375 4.375H.938ZM11.25 19.063a.313.313 0 0 1-.313.312h-10a.312.312 0 0 1-.312-.313v-10a.312.312 0 0 1 .313-.312H11.25v10.313Z"></path>
            </g>
            <defs>
              <clipPath id="fullscreenExpand_svg__a">
                <path fill="#fff" d="M0 0h20v20H0z"></path>
              </clipPath>
            </defs>
          </svg>
        </button>
      </div>
    </div>
    <p><br></p>
    <p><br></p>
    <p>
      Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати
      бінарну купу.
    </p>
    <p><br></p>
    <pre class="ql-blockquote" spellcheck="false"> 👉🏻 Примітка. Суть завдання полягає у створенні дерева із купи.
</pre>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 5. Візуалізація обходу бінарного дерева</strong>
    </p>
    <p><br></p>
    <p>
      Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно
      створити програму на Python, яка візуалізує обходи дерева: у глибину та в
      ширину.
    </p>
    <p><br></p>
    <p>
      Вона повинна відображати кожен крок у вузлах з різними кольорами,
      використовуючи 16-систему RGB (приклад
      <code><strong>#1296F0</strong></code>). Кольори вузлів мають змінюватися від темних до світлих відтінків,
      залежно від послідовності обходу. Кожен вузол при його відвідуванні має
      отримувати унікальний колір, який візуально відображає порядок обходу.
    </p>
    <p><br></p>
    <pre class="ql-blockquote" spellcheck="false">👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію
</pre>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 6. Жадібні алгоритми та динамічне програмування</strong>
    </p>
    <p><br></p>
    <p>
      Необхідно написати програму на Python, яка використовує два підходи —
      жадібний алгоритм та алгоритм динамічного програмування для розв’язання
      задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого
      бюджету.
    </p>
    <p><br></p>
    <p>
      Кожен вид їжі має вказану вартість і калорійність. Дані про їжу
      представлені у вигляді словника, де ключ — назва страви, а значення — це
      словник з вартістю та калорійністю.
    </p>
    <p><br></p>
    <div class="ql-syntax-block">
      <pre class="ql-syntax hljs language-ebnf" spellcheck="false" data-highlighted="yes"><span class="hljs-attribute">items</span> = {
    <span class="hljs-string">"pizza"</span>: {<span class="hljs-string">"cost"</span>: 50, <span class="hljs-string">"calories"</span>: 300},
    <span class="hljs-string">"hamburger"</span>: {<span class="hljs-string">"cost"</span>: 40, <span class="hljs-string">"calories"</span>: 250},
    <span class="hljs-string">"hot-dog"</span>: {<span class="hljs-string">"cost"</span>: 30, <span class="hljs-string">"calories"</span>: 200},
    <span class="hljs-string">"pepsi"</span>: {<span class="hljs-string">"cost"</span>: 10, <span class="hljs-string">"calories"</span>: 100},
    <span class="hljs-string">"cola"</span>: {<span class="hljs-string">"cost"</span>: 15, <span class="hljs-string">"calories"</span>: 220},
    <span class="hljs-string">"potato"</span>: {<span class="hljs-string">"cost"</span>: 25, <span class="hljs-string">"calories"</span>: 350}
}
</pre>
      <button class="copy"></button>
    </div>
    <p><br></p>
    <p>
      Розробіть функцію <code><strong>greedy_algorithm</strong></code> жадібного
      алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до
      вартості, не перевищуючи заданий бюджет.
    </p>
    <p>
      Для реалізації алгоритму динамічного програмування створіть функцію
      <code><strong>dynamic_programming</strong></code>, яка обчислює оптимальний набір страв для максимізації калорійності при
      заданому бюджеті.
    </p>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Завдання 7. Використання методу Монте-Карло</strong>
    </p>
    <p><br></p>
    <p>
      Необхідно написати програму на Python, яка імітує велику кількість кидків
      кубиків, обчислює суми чисел, які випадають на кубиках, і визначає
      ймовірність кожної можливої суми.
    </p>
    <p><br></p>
    <p>
      Створіть симуляцію, де два кубики кидаються велику кількість разів. Для
      кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте,
      скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі
      симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
    </p>
    <p><br></p>
    <p>
      На основі проведених імітацій створіть таблицю або графік, який відображає
      ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
    </p>
    <p><br></p>
    <p>
      Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним
      чином.
    </p>
    <p><br></p>
    <div class="ql-custom-image" contenteditable="false" align="center" data-blot-name="custom-image" data-id="ipqe8" data-src="https://s3.eu-north-1.amazonaws.com/lms.goit.files/dba25f8d-4764-46dc-bc57-6fc51c4e782a120.png" data-width="300px" data-height="auto">
      <div class="next-1bk4wn6 e11xll1g1">
        <img class="ql-custom-image" id="ipqe8" src="https://s3.eu-north-1.amazonaws.com/lms.goit.files/dba25f8d-4764-46dc-bc57-6fc51c4e782a120.png"><button>
          <svg viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">
            <g clip-path="url(#fullscreenExpand_svg__a)" fill="currentcolor">
              <path d="M20 19.063V.938A.939.939 0 0 0 19.062 0H.938A.939.939 0 0 0 0 .938v5.625a.312.312 0 1 0 .625 0V.938A.313.313 0 0 1 .938.625h18.125a.313.313 0 0 1 .312.313v18.125a.313.313 0 0 1-.313.312h-5.625a.313.313 0 1 0 0 .625h5.626c.516 0 .937-.42.937-.938Z"></path>
              <path d="M.938 8.125A.939.939 0 0 0 0 9.063v10c0 .516.42.937.938.937h10c.516 0 .937-.42.937-.938V8.568l4.375-4.375v4.245a.312.312 0 1 0 .625 0v-5a.312.312 0 0 0-.313-.312h-5a.313.313 0 1 0 0 .625h4.245l-4.375 4.375H.938ZM11.25 19.063a.313.313 0 0 1-.313.312h-10a.312.312 0 0 1-.312-.313v-10a.312.312 0 0 1 .313-.312H11.25v10.313Z"></path>
            </g>
            <defs>
              <clipPath id="fullscreenExpand_svg__a">
                <path fill="#fff" d="M0 0h20v20H0z"></path>
              </clipPath>
            </defs>
          </svg>
        </button>
      </div>
    </div>
    <p><br></p>
    <p>
      Порівняйте отримані за допомогою методу Монте-Карло результати з
      аналітичними розрахунками, наведеними в таблиці вище.
    </p>
    <p><br></p>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Підготовка та завантаження фінального проєкту</strong>
    </p>
    <p><br></p>
    <p>1. Створіть публічний репозиторій&nbsp;<code>goit-algo-fp</code>.</p>
    <p>2. Виконайте завдання та відправте його у свій репозиторій.</p>
    <p>
      3. Завантажте робочі файли на свій комп’ютер та прикріпіть їх у LMS у
      форматі&nbsp;<code>zip</code>. Назва архіву повинна бути у форматі
      ФП_<em>ПІБ</em>.
    </p>
    <p>
      4. Прикріпіть посилання на репозиторій&nbsp;<code>goit-algo-fp</code> та
      відправте на перевірку.
    </p>
    <p><br></p>
    <p><br></p>
    <p><strong class="ql-size-large">Формат здачі</strong></p>
    <p><br></p>
    <ul>
      <li>
        Прикріплені файли репозиторію у форматі&nbsp;<code>zip</code> з назвою
        ФП_<em>ПІБ.</em>
      </li>
      <li>Посилання на репозиторій.</li>
    </ul>
    <p><br></p>
    <p><br></p>
    <p>
      <strong class="ql-size-large">Критерії прийняття фiнального проєкту</strong>
    </p>
    <p><br></p>
    <p><strong>Завдання 1:</strong></p>
    <p>
      - Реалізовано функцію реверсування однозв'язного списку, яка змінює
      посилання між вузлами. Код виконується.
    </p>
    <p><br></p>
    <p>
      - Програмно реалізовано алгоритм сортування (функцію) для однозв'язного
      списку. Код виконується.
    </p>
    <p><br></p>
    <p>
      - Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в
      один відсортований список. Код виконується.
    </p>
    <p><br></p>
    <p><strong>Завдання 2:</strong></p>
    <p>- Код виконується. Програма візуалізує фрактал “дерево Піфагора”.</p>
    <p><br></p>
    <p>-Користувач має можливість вказати рівень рекурсії.</p>
    <p><br></p>
    <p><strong>Завдання 3:</strong></p>
    <p>
      - Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого
      шляху у графі з використанням бінарної купи (піраміди).
    </p>
    <p><br></p>
    <p>
      - У межах реалізації завдання створено граф, використано піраміду для
      оптимізації вибору вершин та виконано обчислення найкоротших шляхів від
      початкової вершини до всіх інших.
    </p>
    <p><br></p>
    <p><strong>Завдання 4:</strong></p>
    <p>- Код виконується. Функція візуалізує бінарну купу.</p>
    <p><br></p>
    <p><strong>Завдання 5:</strong></p>
    <p>
      - Програмно реалізовано алгоритми DFS і BFS для візуалізації обходу дерева
      в глибину та в ширину. Використано стек та чергу.
    </p>
    <p><br></p>
    <p>
      - Кольори вузлів змінюються від темних до світлих відтінків залежно від
      порядку обходу.
    </p>
    <p><br></p>
    <p><strong>Завдання 6:</strong></p>
    <p>
      - Програмно реалізовано функцію, яка використовує принцип жадібного
      алгоритму. Код виконується і повертає назви страв, максимізуючи
      співвідношення калорій до вартості, не перевищуючи заданий бюджет.
    </p>
    <p><br></p>
    <p>- Програмно реалізовано функцію, яка використовує принцип динамічного</p>
    <p>
      програмування. Код виконується і повертає оптимальний набір страв для
      максимізації калорійності при заданому бюджеті.
    </p>
    <p><br></p>
    <p><strong>Завдання 7:</strong></p>
    <p>
      - Програмно реалізовано алгоритм для моделювання кидання двох ігрових
      кубиків і побудови таблиці сум та їх імовірностей за допомогою методу
      Монте-Карло.
    </p>
    <p><br></p>
    <p>
      - Код виконується та імітує велику кількість кидків кубиків, обчислює суми
      чисел, які випадають на кубиках, підраховує, скільки разів кожна можлива
      сума з’являється у процесі симуляції, і визначає ймовірність кожної
      можливої суми.
    </p>
    <p><br></p>
    <p>
      - Створено таблицю або графік, який відображає ймовірності кожної суми,
      виявлені за допомогою методу Монте-Карло.
    </p>
    <p><br></p>
    <p>
      - Зроблено висновки щодо правильності розрахунків шляхом порівняння
      отриманих за допомогою методу Монте-Карло результатів та результатів
      аналітичних розрахунків. Висновки оформлено у вигляді файлу
      <code>readme.md</code> фінального завдання.
    </p>
    <p><br></p>
    <p><br></p>
    <p><strong class="ql-size-large">Формат оцінювання:</strong></p>
    <p><br></p>
    <p>Оцінка від 0 до 100.</p>
    <p>Завдання 1 оцінюється в 15 балів.</p>
    <p>Завдання 2 оцінюється в 15 балів.</p>
    <p>Завдання 3 оцінюється в 10 балів.</p>
    <p>Завдання 4 оцінюється в 15 балів.</p>
    <p>Завдання 5 оцінюється в 15 балів.</p>
    <p>Завдання 6 оцінюється в 15 балів.</p>
    <p>Завдання 7 оцінюється в 15 балів.</p>
  </div>
</div>

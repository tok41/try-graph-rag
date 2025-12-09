# Try GraphRAG

## 目的

- Graphを理解することと、GraphRAGを試してみることが目的

## 技術スタック

- NetworkX: グラフの構築と可視化
- Neo4j: グラフDB。グラフ構造の永続化。
- Cypher: グラフクエリ言語
- langchain: RAGフレームワーク
- OpenAI API: LLM

## やること

| フェーズ | 内容 | 主なツール | ゴール |
|--------|------|-----------|--------|
| **1. グラフ構造に慣れる** | 手動でノード・エッジを作成・描画 | `networkx`, `matplotlib` | グラフ構造の直感的理解 |
| **2. 簡易データから知識グラフを作る** | テキスト→トリプル抽出（手動 or LLM） | `Python`, `networkx` | 小規模知識グラフを構築 |
| **3. グラフ検索・解析を試す** | 近傍探索・最短経路・中心性など | `networkx` | グラフ検索と構造分析に慣れる |
| **4. Neo4jへ永続化＋可視化** | グラフDBへ投入・Cypherクエリ実践 | `Neo4j`, `Cypher` | グラフDB操作とクエリ構築を習得 |
| **5. Graph RAGを構築・比較** | LangChain + Neo4jでGraph RAG実装 | `LangChain`, `Neo4j`, `OpenAI API` | 通常RAGとの比較でGraph RAGの効果を理解 |

- フェーズ3については、フェーズ2の中で試したので飛ばす
  - `notebooks/phase_2_knowledge_graph_handwrite.ipynb` 参照

## 環境構築

ここでは、 [uv](https://github.com/astral-sh/uv) を利用した環境構築を例にします。パッケージ管理については利用の環境に合わせてください。

(必要なら) uv のインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env  # または、ターミナルの再起動
```

プロジェクト作成

```bash
# clone this repository

# （必要なら）python 3.12 を uv で用意
uv python install 3.12   # 初回だけ

cd try-graph-rag
uv sync
```

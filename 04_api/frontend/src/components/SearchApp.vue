<template>
    <div class="search-app">
      <h1>Busca de Operadoras</h1>
      
      <!-- Campo para digitar o nome da operadora -->
      <div class="controls">
        <input
          v-model="query"
          type="text"
          placeholder="Digite o nome da operadora"
          @keydown.enter="onKeyDown"
        />
        
        <!-- Campo para selecionar o número máximo de resultados -->
        <div class="select-container">
          <label for="maxResults">Máximo de resultados:</label>
          <select v-model="maxResults" id="maxResults">
            <option value="1">1</option>
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="20">20</option>
            <option value="30">30</option>
            <option value="50">50</option>
          </select>
        </div>
        <button @click="searchOperadoras">Buscar</button>
      </div>
  
      <!-- Resultados da busca -->
      <div class="results-container">
        <li
          v-for="(operadora, index) in results"
          :key="index"
          :class="{'show-details': operadora.showDetails}"
        >
          <p><strong>{{ operadora.razao_social }}</strong></p>
          <p>{{ operadora.nome_fantasia }}</p>
          <button @click="toggleDetails(operadora)">Ver mais detalhes</button>
          <div class="details" v-if="operadora.showDetails">
            <p><strong>CNPJ:</strong> {{ operadora.cnpj }}</p>
            <p><strong>Modalidade:</strong> {{ operadora.modalidade }}</p>
            <p><strong>Telefone:</strong> {{ operadora.telefone }}</p>
            <p><strong>Endereço:</strong> {{ operadora.logradouro }}, {{ operadora.numero }}, {{ operadora.bairro }}</p>
          </div>
        </li>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "SearchApp",
    data() {
      return {
        query: "",
        maxResults: 10, // Número máximo de resultados padrão
        results: [], // Resultados da busca
      };
    },
    methods: {
      onKeyDown(event) {
        if (event.key === "Enter") {
          this.searchOperadoras(); // Executa a busca quando a tecla Enter for pressionada
        }
      },
      async searchOperadoras() {
        if (this.query.length === 0) {
          this.results = []; // Limpar resultados se a busca estiver vazia
          return;
        }
        try {
          const response = await axios.get("http://localhost:8000/search", {
            params: {
              query: this.query, // Passar o termo da busca
              maxResults: this.maxResults, // Passar o número máximo de resultados
            },
          });
          this.results = response.data.results.map(operadora => ({
            ...operadora,
            showDetails: false, // Inicializa todos com detalhes escondidos
          }));
        } catch (error) {
          console.error("Erro ao buscar operadoras:", error);
        }
      },
      toggleDetails(operadora) {
        operadora.showDetails = !operadora.showDetails; // Alterna a visibilidade dos detalhes
      },
    },
  };
  </script>
  
  <style scoped>
  .search-app {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    font-family: "Arial", sans-serif;
    background: #faf6ff;
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    text-align: center;
  }
  
  h1 {
    color: #4a148c; /* Roxo mais sóbrio para título */
    font-size: 28px;
    margin-bottom: 20px;
  }
  
  .controls {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
    gap: 20px; /* Adiciona espaçamento entre os controles */
  }
  
  input {
    flex-grow: 2;
    padding: 12px;
    font-size: 16px;
    border: 2px solid #d1a9f0;
    border-radius: 8px;
    background: #fff;
    outline: none;
    transition: 0.3s;
    min-width: 250px; /* Definindo uma largura mínima */
  }
  
  input:focus {
    border-color: #9b59b6;
    box-shadow: 0 0 6px rgba(155, 89, 182, 0.6);
  }
  
  .select-container {
    display: flex;
    align-items: center;
    gap: 10px; /* Adiciona espaço entre o label e o select */
  }
  
  select {
    padding: 8px;
    font-size: 16px;
    border-radius: 8px;
    border: 1px solid #d1a9f0;
    width: 120px; /* Definindo uma largura fixada */
    background: #fff;
    transition: 0.3s;
  }
  
  select:focus {
    border-color: #9b59b6;
    box-shadow: 0 0 6px rgba(155, 89, 182, 0.6);
  }
  
  button {
    background-color: #4a148c; /* Cor mais sóbria para o botão */
    color: white;
    border: none;
    padding: 10px 14px;
    margin-bottom: 10px;
    cursor: pointer;
    border-radius: 8px;
    font-size: 14px;
    transition: 0.3s;
    min-width: 100px; /* Definindo um tamanho mínimo para o botão */
  }
  
  button:hover {
    background-color: #6a0dad;
    transform: scale(1.05);
  }
  
  .results-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(380px, 1fr)); /* Layout responsivo */
    gap: 20px;
    justify-items: center; /* Centraliza os cards */
  }
  
  li {
    padding: 16px;
    border: none;
    margin-bottom: 12px;
    border-radius: 12px;
    background: #fff;
    box-shadow: 4px 4px 12px rgba(0, 0, 0, 0.1);
    text-align: center;
    transition: all 0.3s ease-in-out;
  }
  
  li:hover {
    transform: scale(1.05);
    box-shadow: 6px 6px 14px rgba(0, 0, 0, 0.15);
  }
  
  .details {
    margin-top: 10px;
    padding: 12px;
    background: rgba(255, 255, 255, 0.9);
    border-radius: 8px;
    border-left: 5px solid #9b59b6;
    box-shadow: inset 2px 2px 8px rgba(0, 0, 0, 0.05);
    display: none; /* Inicialmente escondido */
  }
  
  li.show-details .details {
    display: block; /* Exibe os detalhes ao clicar */
  }
  </style>
  
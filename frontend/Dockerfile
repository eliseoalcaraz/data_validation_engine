FROM node:20

WORKDIR /app

ARG REACT_APP_API_URL=http://backend:8000

ENV REACT_APP_API_URL=$REACT_APP_API_URL

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]

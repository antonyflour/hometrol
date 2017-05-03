<?php

/**
 * Created by PhpStorm.
 * User: anton
 * Date: 03/05/2017
 * Time: 11:52
 */
class Pin
{
    private $numero;
    private $tipo;
    private $nome;
    private $usato;
    private $out_mode;
    private $in_mode;
    private $stato;

    /**
     * Pin constructor.
     * @param $numero
     * @param $tipo
     * @param $nome
     * @param $usato
     * @param $out_mode
     * @param $in_mode
     * @param $stato
     */
    public function __construct($numero, $tipo, $nome, $usato, $out_mode, $in_mode, $stato)
    {
        $this->numero = $numero;
        $this->tipo = $tipo;
        $this->nome = $nome;
        $this->usato = $usato;
        $this->out_mode = $out_mode;
        $this->in_mode = $in_mode;
        $this->stato = $stato;
    }

    /**
     * @return mixed
     */
    public function getNumero()
    {
        return $this->numero;
    }

    /**
     * @param mixed $numero
     */
    public function setNumero($numero)
    {
        $this->numero = $numero;
    }

    /**
     * @return mixed
     */
    public function getTipo()
    {
        return $this->tipo;
    }

    /**
     * @param mixed $tipo
     */
    public function setTipo($tipo)
    {
        $this->tipo = $tipo;
    }

    /**
     * @return mixed
     */
    public function getNome()
    {
        return $this->nome;
    }

    /**
     * @param mixed $nome
     */
    public function setNome($nome)
    {
        $this->nome = $nome;
    }

    /**
     * @return mixed
     */
    public function getUsato()
    {
        return $this->usato;
    }

    /**
     * @param mixed $usato
     */
    public function setUsato($usato)
    {
        $this->usato = $usato;
    }

    /**
     * @return mixed
     */
    public function getOutMode()
    {
        return $this->out_mode;
    }

    /**
     * @param mixed $out_mode
     */
    public function setOutMode($out_mode)
    {
        $this->out_mode = $out_mode;
    }

    /**
     * @return mixed
     */
    public function getInMode()
    {
        return $this->in_mode;
    }

    /**
     * @param mixed $in_mode
     */
    public function setInMode($in_mode)
    {
        $this->in_mode = $in_mode;
    }

    /**
     * @return mixed
     */
    public function getStato()
    {
        return $this->stato;
    }

    /**
     * @param mixed $stato
     */
    public function setStato($stato)
    {
        $this->stato = $stato;
    }



}
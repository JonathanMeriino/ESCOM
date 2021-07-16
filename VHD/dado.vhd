library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;

entity dado is port(
	
	clk,en: in std_logic;                 
	sal: out std_logic_vector(2 downto 0));
	
end dado;

architecture dados of dado is

type estado is (num1, num2, num3, num4, num5, num6);
signal presente, futuro: estado;
 begin

	proceso_clk: 
	process (clk) begin
		if (clk'event and clk='1') then
			presente <= futuro;
		end if;
	end process proceso_clk;

	proceso_d: process (presente, en) begin
	case presente is
	when num1 =>
			if en = '0' then
				futuro <= num2;
				sal <= "010";
			else
				futuro <= num1;
				sal <= "001";--1
			end if;
	when num2 =>
			if en = '0' then
				futuro <= num3;
				sal <= "011";
			else
				futuro <= num2;
				sal <= "010";--2
			end if;
	when num3 =>
			if en = '0' then
				futuro <= num4;
				sal <= "100";
			else
				futuro <= num3;
				sal <= "011";--3
			end if;
	when num4 =>
			if en = '0' then
				futuro <= num5;
				sal <= "101";
			else
				futuro <= num4;
				sal <= "100";--4
			end if;
	when num5 =>
			if en = '0' then
				futuro <= num6;
				sal <= "110";
			else
				futuro <= num5;
				sal <= "101"; --5
			end if;
	when num6 =>
			if en = '0' then
				futuro <= num1;
				sal <= "001";
			else
				futuro <= num6;
				sal <= "110"; --6
			end if;
	end case;
	
	end process proceso_d;
end dados;
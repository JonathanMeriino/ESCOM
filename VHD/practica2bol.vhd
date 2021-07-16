library ieee;
use ieee.std_logic_1164.all;
use work.std_arith.all;
entity boleta is port(
	en,clk: in std_logic;                 
	d: out std_logic_vector(3 downto 0);
	aux: out std_logic_vector (3 downto 0));
				
end boleta;
architecture no_boleta of boleta is

 begin
	process (clk) begin
		if (clk'event and clk='1')then
			aux <= aux+1;
			if (aux="1001") then
				aux<="0000";
			 end if;
		end if;
	end process;
	process (aux) begin
	case aux is
	
	when "0000"=>
	        if en ='0' then
			d <= "0010"; --2
			elsif en ='1' then
			d <= "0010"; --2
			end if;
	when "0001"=>
		if en ='0' then
			d <= "0000"; --0
			elsif en ='1' then
			d <= "0000";--0
			end if;
	when "0010"=>
		if en ='0' then
			d <= "0011"; --3
			elsif en ='1' then
			d <= "0100"; --4
			end if;
	when "0011"=>
		if en ='0' then
			d <= "0100";--4
			elsif en ='1' then
			d <= "0110";--6
			end if;
	when "0100"=>
		if en ='0' then
			d <= "0001";--1
			elsif en ='1' then
			d <= "1000";--8
			end if;
	when "0101"=>
			if en ='0' then
			d <= "0101";--5
			elsif en ='1' then
			d <= "0111";--7
			end if;
	when "0110"=>
		if en ='0' then
			d <= "0111"; --7
			elsif en ='1' then
			d <= "0011"; --3
			end if;
	when "0111"=>
	        if en ='0' then
			d <= "1001"; --9
			elsif en ='1' then
			d <= "0101"; --5
			end if;
	when "1000"=>
	        if sw ='0' then
			d <= "0110"; --6
			elsif en ='1' then
			d <= "1001"; --9
			end if;
	when "1001"=>
	        if en ='0' then
			d <= "0011"; --3
			elsif en ='1' then
			d <= "0000"; --1
			end if;
	when others=> 
            if en ='0' then
			d <= "0010"; 
			elsif en ='1' then
			d <= "0010"; 
			end if;
	end case;
	end process;
end no_boleta;
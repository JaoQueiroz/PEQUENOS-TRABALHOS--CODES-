import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ContaBanco contaT = new ContaBanco();
        System.out.println(" Por favor, digite o número da Conta !");
        contaT.numero = sc.nextInt();
        System.out.println(" Por favor, digite o número da Agência !");
        contaT.agencia = sc.nextLine();
        sc.nextLine();
        System.out.println(" Por favor, digite seu Nome!");
        contaT.nomeCliente = sc.nextLine();
        System.out.println(" Por favor, quanto deseja Depositar!");
        contaT.saldo = sc.nextDouble();
        sc.nextLine();

        System.out.printf("Olá %s, obrigado por criar uma conta em nosso banco, sua agência é %s, conta %d e seu saldo %.2f já está disponível para saque.",
                contaT.nomeCliente, contaT.agencia, contaT.numero, contaT.saldo);


        sc.close();

    }
}
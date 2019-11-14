package som;
import java.applet.Applet;
import java.awt.Graphics;
import java.awt.Canvas;
import java.awt.Color;
import java.awt.Frame;
import java.awt.event.KeyListener;
import java.awt.event.KeyEvent;

import javax.swing.JFrame;

//全ての色を変更するsom
public class Som extends Canvas implements KeyListener{
	
	int N = 20;
	Color[][] color = new Color[N][N];
	int count = 0;
	
	public Som() {
		addKeyListener(this);
		setSize(700, 700);
		setBackground(Color.white);
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				color[i][j] = new Color((int)(Math.random()*256), (int)(Math.random()*256), (int)(Math.random()*256));
			}
		}
	}
	
	public void paint (Graphics g){
		g.setColor(Color.black);
		g.drawString(String.valueOf(count), 30, 20);
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				g.setColor(color[i][j]);
				g.fillRect(i*30+30, j*30+30, 30, 30);
			}
		}
		requestFocusInWindow();
	}
	
	public static void main(String[] args) {
		Som canvas = new Som();
		JFrame frame = new JFrame("Som");
		
		frame.add(canvas);
		frame.setSize(750, 750);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setVisible(true);
	}
	
	@Override
	public void keyPressed(KeyEvent e) {
		// TODO Auto-generated method stub
		int keycode = e.getKeyCode();
		if(keycode == KeyEvent.VK_ENTER) {
			Color element = new Color((int)(Math.random()*256), (int)(Math.random()*256), (int)(Math.random()*256));
			int[] coordinate = euclidean(element);
			exposure(coordinate, element);
			
			count++;
			repaint();
		}
		else if(keycode == KeyEvent.VK_A) {
			for (int i = count; i < 10000; i++) {
				Color element = new Color((int)(Math.random()*256), (int)(Math.random()*256), (int)(Math.random()*256));
				int[] coordinate = euclidean(element);
				exposure(coordinate, element);
				count++;
				repaint();
			}
		}
		else if(keycode == KeyEvent.VK_1) {
			for (int i = 0; i < 1000; i++) {
				Color element = new Color((int)(Math.random()*256), (int)(Math.random()*256), (int)(Math.random()*256));
				int[] coordinate = euclidean(element);
				exposure(coordinate, element);
				count++;
				repaint();
			}
		}
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}
	
	//ユークリッド距離が最小の座標を返す
	private int[] euclidean(Color element) {
		int[] coordinate = {0, 0};
		double min = 100000000;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				double value = Math.sqrt(Math.pow(color[i][j].getRed() - element.getRed(), 2) + Math.pow(color[i][j].getGreen() - element.getGreen(), 2) + Math.pow(color[i][j].getBlue() - element.getBlue(), 2));
				if(value < min) {
					min = value;
					coordinate[0] = i;
					coordinate[1] = j;
				}
			}
		}
		return coordinate;
	}
	
	private void exposure(int[] coordinate, Color element) {
		double L0 = 0.1;
		double sigma0 = 10;
		double rambda = 2500;
		double Lt = L0 * Math.exp(-count / rambda);
		double sigma = sigma0 * Math.exp(-count / rambda);
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				double shita = Math.exp(-(Math.pow(i-coordinate[0], 2)+Math.pow(j-coordinate[1], 2)) / (2 * Math.pow(sigma, 2)));
				color[i][j] = new Color((int)Math.round(color[i][j].getRed() + shita * Lt * (element.getRed() - color[i][j].getRed())), (int)Math.round(color[i][j].getGreen() + shita * Lt * (element.getGreen() - color[i][j].getGreen())), (int)Math.round(color[i][j].getBlue() + shita * Lt * (element.getBlue() - color[i][j].getBlue())));
			}
		}
	}
}